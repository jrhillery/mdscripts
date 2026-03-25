package gz.jythonhelper;

import java.io.*;
import java.lang.reflect.Constructor;
import java.lang.reflect.Executable;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Downloaded from <a href="https://github.com/kaneg/JythonHelper">GitHub</a>
 * Date: 1/28/24
 */
public class EasyJython {

    public static final Pattern PATTERN_FROM_IMPORT = Pattern.compile("\\s*from\\s*(\\S+)\\s*import\\s+(\\w[\\w, \\t]*)");

    public static final Pattern PATTERN_IMPORT = Pattern.compile("\\s*import\\s*(\\S+)");

    public static final Pattern PATTERN_FROM_IMPORT_MULTIPLE = Pattern.compile("\\s*from\\s*(\\S+)\\s*import\\s+\\(\\s*(.*)\\s*\\)", Pattern.MULTILINE);

    public static final String[] PREDEFINED_CLASSES = {};

    public static final String USER_HOME = System.getProperty("user.home");

    ClassGenerator cg;
    private ClassLoader classLoader;

    public EasyJython(String outputDir) {
        cg = new PyClassGenerator(outputDir);
    }

    public void setLibs(String[] libs) {
        List<URL> urls = new ArrayList<>();
        for (String name : libs) {
            try {
                if (name.endsWith("*")) {
                    name = name.substring(0, name.length() - 1);
                }
                File file = new File(name);
                if (file.isDirectory()) {
                    File[] files = file.listFiles(
                       pathname -> pathname.isFile() && pathname.getName().toLowerCase().endsWith(".jar"));
                    if (files != null) {
                        for (File f : files) {
                            urls.add(f.toURI().toURL());
                        }
                    }
                } else {
                    urls.add(file.toURI().toURL());
                }
            } catch (MalformedURLException e) {
                e.printStackTrace(System.err);
            }
        }
        classLoader = new URLClassLoader(urls.toArray(new URL[0]));
    }

    public void generatePys(String... pyFiles) {
       Set<String> classList = new TreeSet<>(Arrays.asList(PREDEFINED_CLASSES));
        for (String f : pyFiles) {
            File file = new File(f);
            if (file.isFile()) {
                System.out.println("File:--->" + file.getName());
                classList.addAll(getClassListFromPy(file));
            } else {
                System.out.println("Directory:--->" + file.getAbsolutePath().replace(USER_HOME, "~"));
                File[] files = file.listFiles((dir, name) -> name.endsWith(".py"));
                if (files != null) {
                    for (File child : files) {
                        System.out.println("--->" + child.getName());
                        classList.addAll(getClassListFromPy(child));
                    }
                }
            }
        }

        for (String className : classList) {
            try {
                System.out.println("Generating:" + className);
                Class<?> clazz = Class.forName(className, false, classLoader);
                System.out.println(clazz);
                cg.createPyForClass(clazz);
            } catch (ClassNotFoundException e) {
                System.out.println("Class not found:" + e.getMessage());
            } catch (IOException e) {
                System.err.println("IO Exception:" + e.getMessage());
            }
        }
    }

    private Set<String> getClassListFromPy(File file) {
        StringBuilder sb = new StringBuilder();
        Set<String> classes = new HashSet<>();
        try {
            String line;
            BufferedReader br = new BufferedReader(new FileReader(file));
            while ((line = br.readLine()) != null) {
                sb.append(line).append("\n");
                Matcher matcher = PATTERN_FROM_IMPORT.matcher(line);
                if (matcher.matches()) {
                    System.out.println(line);
                    String packageName = matcher.group(1);
                    String classSimpleName = matcher.group(2);
                    String[] names = classSimpleName.split(",");//for from xyz import Abc, Def, Ghi
                    for (String className : names) {
                        className = className.trim();
                        if (!className.isEmpty()) {
                            String[] split = className.split(" ");// for import Abc as abc
                            className = split[0].trim();
                            classes.add(packageName + "." + className);
                        }
                    }
                    continue;
                }

                matcher = PATTERN_IMPORT.matcher(line);
                if (matcher.matches()) {
                    String classSimpleName = matcher.group(1);
                    classes.add(classSimpleName);
                }
            }
            br.close();
            Matcher matcher = PATTERN_FROM_IMPORT_MULTIPLE.matcher(sb.toString());
            while (matcher.find()) {
                String packageName = matcher.group(1);
                String classSimpleName = matcher.group(2);
                String[] names = classSimpleName.split(",");//for from xyz import Abc, Def, Ghi
                for (String className : names) {
                    className = className.trim();
                    if (!className.isEmpty()) {
                        String[] split = className.split(" ");// for import Abc as abc
                        className = split[0].trim();
                        classes.add(packageName + "." + className);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace(System.err);
        }
        return classes;
    }
}

abstract class ClassGenerator {
    public static final String LINE_SEPARATOR = "\n";
    public static final String INIT_PY = "__init__.py";
    public static final String DEF_TPL = "def %s(%s):";
    public static final String CLASS_TPL = "class %s(%s):" + LINE_SEPARATOR;
    public static final String SOURCE_TPL = "# source:%s" + LINE_SEPARATOR;
    public static final String PASS = "pass";
    private static final String INDENT = "    ";
    public static final String STATIC_METHOD = "@staticmethod" + LINE_SEPARATOR;

    public static final Set<String> IGNORED_FIELDS = new HashSet<>(List.of("in"));
    public static final Set<String> IGNORED_METHODS = new HashSet<>(Arrays.asList(
       "wait", "hashCode", "notify", "notifyAll", "yield",
       "and", "from", "is", "not", "or", "print", "with"));

    public static final String USER_HOME_SLASH = EasyJython.USER_HOME.replace('\\', '/');
    private final String outputDir;
    public static final String INIT_TEMPLATE = """
       # encoding: utf-8
       # module %s
       """;
//       # from (built-in)
//       # by generator 999.999

    protected ClassGenerator(String outputDir) {
        this.outputDir = outputDir;
    }

    String indent(String line) {
        return indent(line, 1);
    }

    String indent(String line, int level) {
       return INDENT.repeat(Math.max(0, level)) + line;
    }

    String makeAField(Field f) {
        return f.getName() + " = None";
    }

    String indents(String line) {
        String[] split = line.split(LINE_SEPARATOR);
        StringBuilder sb = new StringBuilder();
        for (String s : split) {
            sb.append(indent(s, 1));
            sb.append(LINE_SEPARATOR);
        }
        return sb.toString();
    }

    void writePyHeader(FileWriter fw, String name) {
        try {
            fw.write(String.format(INIT_TEMPLATE, name));
        } catch (IOException e) {
            e.printStackTrace(System.err);
        }
    }

    void ensureInitPy(File dir) {
        File initFile = new File(dir, INIT_PY);
        if (!initFile.exists()) {
            try {
                boolean newFile = initFile.createNewFile();
                if (newFile) {
                    FileWriter fw = new FileWriter(initFile);
                    writePyHeader(fw, initFile.getName());
                    fw.close();
                }
            } catch (IOException e) {
                e.printStackTrace(System.err);
            }
        }
    }

    File createDirectory(Class<?> clazz) {
        String packageName = clazz.getPackage().getName();
        System.out.println("create package directory:" + packageName);

        String[] split = packageName.split("\\.");
        File currentDir = new File(outputDir);
        for (String dirName : split) {
            File tmpDir = new File(currentDir, dirName);
            if (!tmpDir.exists()) {
                if (!tmpDir.mkdir()) {
                    System.out.println("Failed to create directory " + tmpDir);
                }
            }
            ensureInitPy(tmpDir);
            currentDir = tmpDir;
        }
        return currentDir;
    }

    <T extends Executable> Collection<T> filterOverrideMethods(T[] methods) {
        Map<String, T> methodMap = new TreeMap<>();

        for (T m : methods) {
            String name = m.getName();
            T existingMethod = methodMap.get(name);
            if (existingMethod == null) {
                methodMap.put(name, m);
            } else {
                Class<?>[] parameterTypes = existingMethod.getParameterTypes();
                Class<?>[] newParameterTypes = m.getParameterTypes();
                if (newParameterTypes.length > parameterTypes.length) {
                    methodMap.put(name, m);
                } else if (newParameterTypes.length == parameterTypes.length) {
                    String signature = existingMethod.toGenericString();
                    String newSignature = m.toGenericString();
                    if (newSignature.compareToIgnoreCase(signature) < 0) {
                        methodMap.put(name, m);
                    }
                }
            }
        }
        return methodMap.values();
    }

    Collection<Class<?>> filterDuplicateClasses(Class<?>[] classes, Class<?> parentClazz) {
        String pkgName = parentClazz.getPackageName();
        Map<String, Class<?>> classMap = new TreeMap<>();

        for (Class<?> c : classes) {
            String name = c.getSimpleName();
            Class<?> existingClass = classMap.get(name);

            if (existingClass == null) {
                classMap.put(name, c);
            } else {
                String newPkgName = c.getPackageName();
                Class<?> ignoredClass;

                if (newPkgName.equals(pkgName)) {
                    classMap.put(name, c);
                    ignoredClass = existingClass;
                } else {
                    ignoredClass = c;
                }
                System.out.println("Ignoring duplicate nested class "
                   + ignoredClass.toGenericString());
            }
        }
        return classMap.values();
    }

    public abstract void createPyForClass(Class<?> clazz) throws IOException;
}

class PyClassGenerator extends ClassGenerator {

    Pattern CLASS_NAME_PATTERN = Pattern.compile("class\\s+(\\w+).*:");

    protected PyClassGenerator(String outputDir) {
        super(outputDir);
    }

    public void createPyForClass(Class<?> clazz) throws IOException {
        File directory = createDirectory(clazz);
        String classContent = generateClassAsPyClass(clazz, null);
        File initPy = new File(directory, INIT_PY);
        Map<String, StringBuilder> classStringMap = readClassesFromInitPy(initPy);
        classStringMap.put(clazz.getSimpleName(), new StringBuilder(classContent));
        writeClassesFromInitPy(classStringMap, initPy);
    }

    private Map<String, StringBuilder> readClassesFromInitPy(File initFile) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(initFile));
        String line;
        boolean inClass = false;
        Map<String, StringBuilder> maps = new TreeMap<>();
        StringBuilder sb = null;
        while ((line = br.readLine()) != null) {
            if (line.startsWith("class")) {
                inClass = true;
                Matcher matcher = CLASS_NAME_PATTERN.matcher(line);
                if (matcher.matches()) {
                    String className = matcher.group(1);
                    sb = new StringBuilder();
                    maps.put(className, sb);
                }
            }
            if (inClass && sb != null) {
                sb.append(line).append(LINE_SEPARATOR);
            }
        }
        br.close();
        return maps;
    }

    private void writeClassesFromInitPy(Map<String, StringBuilder> classStringMap, File initPy) throws IOException {
        FileWriter fileWriter = new FileWriter(initPy);
        writePyHeader(fileWriter, initPy.getName());
        for (StringBuilder classContent : classStringMap.values()) {
            fileWriter.write(classContent.toString());
        }
        fileWriter.close();
    }

    private String generateClassAsPyClass(Class<?> clazz, Class<?> parentClazz) {
        StringBuilder sb = new StringBuilder();
        sb.append(generatePyClassDeclaration(clazz));
        ClassLoader classLoader = clazz.getClassLoader();
        URL resourceURL = null;
        if (classLoader != null) {
            resourceURL = classLoader.getResource(clazz.getName().replace('.', '/') + ".class");
        }
        if (resourceURL != null) {
            sb.append(indent(String.format(SOURCE_TPL,
               resourceURL.toString().replace(USER_HOME_SLASH, "~"))));
        }
        Field[] fields = new Field[0];
        try {
            fields = clazz.getFields();
        } catch (SecurityException e) {
            e.printStackTrace(System.err);
        }
        Arrays.sort(fields, Comparator.comparing(Field::getName));

        for (Field f : fields) {
            int modifiers = f.getModifiers();
            if (Modifier.isPublic(modifiers)) {
                if (!IGNORED_FIELDS.contains(f.getName())) {
                    sb.append(indent(makeAField(f)));
                    sb.append(LINE_SEPARATOR);
                }
            }
        }
        sb.append(LINE_SEPARATOR);
        Class<?>[] classes = new Class[0];
        try {
            classes = clazz.getClasses();
        } catch (Exception e) {
            e.printStackTrace(System.err);
        }
        if (classes.length > 0 && parentClazz != null && parentClazz.isAssignableFrom(clazz)) {
            System.out.println("Found recursively nested class definition: " + clazz);
        } else {
            Collection<Class<?>> uniqueClasses = filterDuplicateClasses(classes, clazz);

            for (Class<?> innerClazz : uniqueClasses) {
                sb.append(indents(generateClassAsPyClass(innerClazz, clazz)));
                sb.append(LINE_SEPARATOR);
            }
        }
        Constructor<?>[] constructors = new Constructor[0];
        try {
            constructors = clazz.getConstructors();
        } catch (SecurityException e) {
            e.printStackTrace(System.err);
        }
        Collection<Constructor<?>> uniqueConstructors = filterOverrideMethods(constructors);

        for (Constructor<?> m: uniqueConstructors) {
            if (Modifier.isPublic(m.getModifiers())) {
                if (m.getParameterCount() > 0) {
                    sb.append(indents(generateMethodForPyClass(m)));
                    sb.append(indent(PASS, 2));
                    sb.append(LINE_SEPARATOR);
                    sb.append(LINE_SEPARATOR);
                }
            }
        }
        Method[] methods = new Method[0];
        try {
            methods = clazz.getMethods();
        } catch (SecurityException e) {
            e.printStackTrace(System.err);
        }
        Collection<Method> uniqueMethods = filterOverrideMethods(methods);

        for (Method m : uniqueMethods) {
            int modifiers = m.getModifiers();
            if (Modifier.isPublic(modifiers)) {
                String name = m.getName();
                if (!IGNORED_METHODS.contains(name)) {
                    sb.append(indents(generateMethodForPyClass(m)));
                    sb.append(indent(PASS, 2));
                    sb.append(LINE_SEPARATOR);
                    sb.append(LINE_SEPARATOR);
                }
            }
        }
        return sb.toString();
    }

    private static String generatePyClassDeclaration(Class<?> clazz) {
        String base;

        if (Throwable.class.isAssignableFrom(clazz)) {
            // avoid warning: Exception doesn't inherit from base 'Exception' class
            base = "Exception";
        } else {
            // avoid warning: Old-style class contains call for super method
            base = "object";
        }
        return String.format(CLASS_TPL, clazz.getSimpleName(), base);
    } // end generatePyClassDeclaration(Class<?>)

    private String generateMethodForPyClass(Executable m) {
        Class<?>[] parameterTypes = m.getParameterTypes();
        StringBuilder sb = new StringBuilder();
        int modifiers = m.getModifiers();
        String prefix = "";
        if (Modifier.isStatic(modifiers)) {
            prefix = STATIC_METHOD;
        } else {
            sb.append("self, ");
        }
        for (int i = 0; i < parameterTypes.length; i++) {
            Class<?> type = parameterTypes[i];
            String typeName;
            if (type.isArray()) {
                typeName = type.getComponentType().getSimpleName();
            } else {
                typeName = type.getSimpleName();
            }
            sb.append(typeName);
            if (i > 0) {
                sb.append(i);
            }
            sb.append("=None");
            if (i < parameterTypes.length - 1) {
                sb.append(", ");
            }
        }
        String name = (m instanceof Constructor<?>) ? "__init__" : m.getName();

        return prefix + String.format(DEF_TPL, name, sb);
    }
}
