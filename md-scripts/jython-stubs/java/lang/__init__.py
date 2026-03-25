# encoding: utf-8
# module __init__.py
class System(object):
    err = None
    out = None

    class Logger(object):
    
        class Level(object):
            ALL = None
            DEBUG = None
            ERROR = None
            INFO = None
            OFF = None
            TRACE = None
            WARNING = None
        
            class EnumDesc(object):
            
                def bootstrapArgs(self, ):
                    pass
            
                def bootstrapArgsList(self, ):
                    pass
            
                def bootstrapMethod(self, ):
                    pass
            
                def constantName(self, ):
                    pass
            
                def constantType(self, ):
                    pass
            
                def equals(self, Object=None):
                    pass
            
                def getClass(self, ):
                    pass
            
                @staticmethod
                def of(ClassDesc=None, String1=None):
                    pass
            
                @staticmethod
                def ofCanonical(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                    pass
            
                @staticmethod
                def ofNamed(DirectMethodHandleDesc=None, String1=None, ClassDesc2=None, ConstantDesc3=None):
                    pass
            
                def resolveConstantDesc(self, Lookup=None):
                    pass
            
                def toString(self, ):
                    pass
        
            def compareTo(self, Enum=None):
                pass
        
            def describeConstable(self, ):
                pass
        
            def equals(self, Object=None):
                pass
        
            def getClass(self, ):
                pass
        
            def getDeclaringClass(self, ):
                pass
        
            def getName(self, ):
                pass
        
            def getSeverity(self, ):
                pass
        
            def name(self, ):
                pass
        
            def ordinal(self, ):
                pass
        
            def toString(self, ):
                pass
        
            @staticmethod
            def valueOf(Class=None, String1=None):
                pass
        
            @staticmethod
            def values():
                pass
    
        def getName(self, ):
            pass
    
        def isLoggable(self, Level=None):
            pass
    
        def log(self, Level=None, ResourceBundle1=None, String2=None, Object3=None):
            pass

    class LoggerFinder(object):
    
        def equals(self, Object=None):
            pass
    
        def getClass(self, ):
            pass
    
        def getLocalizedLogger(self, String=None, ResourceBundle1=None, Module2=None):
            pass
    
        def getLogger(self, String=None, Module1=None):
            pass
    
        @staticmethod
        def getLoggerFinder():
            pass
    
        def toString(self, ):
            pass

    @staticmethod
    def arraycopy(Object=None, int1=None, Object2=None, int3=None, int4=None):
        pass

    @staticmethod
    def clearProperty(String=None):
        pass

    @staticmethod
    def console():
        pass

    @staticmethod
    def currentTimeMillis():
        pass

    def equals(self, Object=None):
        pass

    @staticmethod
    def exit(int=None):
        pass

    @staticmethod
    def gc():
        pass

    def getClass(self, ):
        pass

    @staticmethod
    def getLogger(String=None, ResourceBundle1=None):
        pass

    @staticmethod
    def getProperties():
        pass

    @staticmethod
    def getProperty(String=None, String1=None):
        pass

    @staticmethod
    def getSecurityManager():
        pass

    @staticmethod
    def getenv(String=None):
        pass

    @staticmethod
    def identityHashCode(Object=None):
        pass

    @staticmethod
    def inheritedChannel():
        pass

    @staticmethod
    def lineSeparator():
        pass

    @staticmethod
    def load(String=None):
        pass

    @staticmethod
    def loadLibrary(String=None):
        pass

    @staticmethod
    def mapLibraryName(String=None):
        pass

    @staticmethod
    def nanoTime():
        pass

    @staticmethod
    def runFinalization():
        pass

    @staticmethod
    def setErr(PrintStream=None):
        pass

    @staticmethod
    def setIn(InputStream=None):
        pass

    @staticmethod
    def setOut(PrintStream=None):
        pass

    @staticmethod
    def setProperties(Properties=None):
        pass

    @staticmethod
    def setProperty(String=None, String1=None):
        pass

    @staticmethod
    def setSecurityManager(SecurityManager=None):
        pass

    def toString(self, ):
        pass

