/*
 * Created on May 10, 2020
 */
package com.moneydance.modules.features.moredecimal;

import static javax.swing.GroupLayout.DEFAULT_SIZE;
import static javax.swing.GroupLayout.PREFERRED_SIZE;

import java.awt.AWTEvent;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.awt.event.WindowEvent;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.ResourceBundle;

import javax.swing.AbstractListModel;
import javax.swing.ComboBoxModel;
import javax.swing.GroupLayout;
import javax.swing.GroupLayout.Alignment;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JComponent;
import javax.swing.JFormattedTextField;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.LayoutStyle.ComponentPlacement;
import javax.swing.SwingUtilities;
import javax.swing.WindowConstants;
import javax.swing.border.EmptyBorder;

import com.infinitekind.moneydance.model.CurrencyTable;
import com.infinitekind.moneydance.model.CurrencyType;
import com.infinitekind.moneydance.model.CurrencyUtil;
import com.leastlogic.swing.util.HTMLPane;

/**
 * More decimal window frame. Edited with WindowBuilder from the Eclipse
 * marketplace.
 */
public class MoreDecimalWindow extends JFrame
		implements ActionListener, FocusListener, MoreDecimalInterface {

	private static class SecurityDataModel extends AbstractListModel<CurrencyType>
			implements ComboBoxModel<CurrencyType> {
		private ArrayList<CurrencyType> securities = new ArrayList<>();
		private Object selectedItem = null;
		private static final long serialVersionUID = -8592081172767823724L;

		public SecurityDataModel(CurrencyTable allCurrencies) {
			for (CurrencyType currency : allCurrencies) {
				if (currency.getCurrencyType() == CurrencyType.Type.SECURITY
						&& !currency.getBooleanParameter("hide_in_ui", false)) {
					this.securities.add(currency);
				}
			} // end for

			this.securities.sort(CurrencyUtil.CURRENCY_TYPENAME_COMPARATOR);

		} // end (CurrencyTable) constructor

		public int getSize() {

			return this.securities.size();
		} // end getSize()

		public CurrencyType getElementAt(int index) {

			return this.securities.get(index);
		} // end getElementAt(int)

		public void setSelectedItem(Object item) {
			if (!equalsSelected(item)) {
				this.selectedItem = item;
				fireContentsChanged(this, -1, -1);
			}

		} // end setSelectedItem(Object)

		private boolean equalsSelected(Object item) {

			if (this.selectedItem == null) {
				return this.selectedItem == item;
			} else {
				return this.selectedItem.equals(item);
			}
		} // end equalsSelected(Object)

		public Object getSelectedItem() {

			return this.selectedItem;
		} // end getSelectedItem()

	} // end class SecurityDataModel

	private Main feature;
	private JComboBox<CurrencyType> securityList;
	private JFormattedTextField fldDecimals;
	private JButton btnStage;
	private JButton btnCommit;
	private HTMLPane pnOutputLog;

	static final String baseMessageBundleName = "com.moneydance.modules.features.moredecimal.MoreDecimalMessages";
	private static final ResourceBundle msgBundle = ResourceBundle.getBundle(baseMessageBundleName);
	private static final NumberFormat txtNumberFmt = NumberFormat.getIntegerInstance();
	private static final long serialVersionUID = -3503760217056404933L;

	/**
	 * Create the frame.
	 *
	 * @param feature
	 * @param allCurrencies
	 */
	public MoreDecimalWindow(Main feature, CurrencyTable allCurrencies) {
		super(msgBundle.getString("MoreDecimalWindow.window.title"));
		this.feature = feature;
		initComponents(allCurrencies);
		wireEvents();

	} // end (Main, CurrencyTable) constructor

	/**
	 * Initialize the swing components.
	 *
	 * @param allCurrencies
	 */
	private void initComponents(CurrencyTable allCurrencies) {
		setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
		setSize(576, 356);
		JPanel contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);

		JLabel lblSecurityToChange = new JLabel(msgBundle.getString("MoreDecimalWindow.lblSecurity.text"));

		this.securityList = new JComboBox<>(new SecurityDataModel(allCurrencies));
		this.securityList.setToolTipText(msgBundle.getString("MoreDecimalWindow.securityList.toolTipText"));

		JLabel lblDecimals = new JLabel(msgBundle.getString("MoreDecimalWindow.lblDecimals.text"));

		this.fldDecimals = new JFormattedTextField(txtNumberFmt);
		this.fldDecimals.setColumns(2);
		this.fldDecimals.setToolTipText(msgBundle.getString("MoreDecimalWindow.fldDecimals.toolTipText"));

		this.btnStage = new JButton(msgBundle.getString("MoreDecimalWindow.btnStage.text"));
		this.btnStage.setEnabled(false);
		this.btnStage.setToolTipText(msgBundle.getString("MoreDecimalWindow.btnStage.toolTipText"));

		this.btnCommit = new JButton(msgBundle.getString("MoreDecimalWindow.btnCommit.text"));
		this.btnCommit.setEnabled(false);
		this.btnCommit.setToolTipText(msgBundle.getString("MoreDecimalWindow.btnCommit.toolTipText"));

		reducePreferredHeight(this.securityList);
		reducePreferredHeight(this.btnStage);
		reducePreferredHeight(this.btnCommit);

		this.pnOutputLog = new HTMLPane();
		JScrollPane scrollPane = new JScrollPane(this.pnOutputLog);

		GroupLayout gl_contentPane = new GroupLayout(contentPane);
		gl_contentPane.setHorizontalGroup(
			gl_contentPane.createParallelGroup(Alignment.TRAILING)
				.addGroup(gl_contentPane.createSequentialGroup()
					.addComponent(lblSecurityToChange)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(this.securityList, PREFERRED_SIZE, 150, Short.MAX_VALUE)
					.addPreferredGap(ComponentPlacement.UNRELATED)
					.addComponent(lblDecimals)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(this.fldDecimals, PREFERRED_SIZE, PREFERRED_SIZE, PREFERRED_SIZE)
					.addPreferredGap(ComponentPlacement.UNRELATED)
					.addComponent(this.btnStage)
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(this.btnCommit))
				.addComponent(scrollPane, DEFAULT_SIZE, 552, Short.MAX_VALUE)
		);
		gl_contentPane.setVerticalGroup(
			gl_contentPane.createParallelGroup(Alignment.LEADING)
				.addGroup(gl_contentPane.createSequentialGroup()
					.addGroup(gl_contentPane.createParallelGroup(Alignment.BASELINE)
						.addComponent(lblSecurityToChange)
						.addComponent(this.securityList)
						.addComponent(lblDecimals)
						.addComponent(this.fldDecimals, PREFERRED_SIZE, DEFAULT_SIZE, PREFERRED_SIZE)
						.addComponent(this.btnStage)
						.addComponent(this.btnCommit))
					.addPreferredGap(ComponentPlacement.RELATED)
					.addComponent(scrollPane, DEFAULT_SIZE, 282, Short.MAX_VALUE))
		);
		contentPane.setLayout(gl_contentPane);

	} // end initComponents(CurrencyTable)

	/**
	 * @param button
	 */
	private void reducePreferredHeight(JComponent button) {
		Dimension textDim = this.fldDecimals.getPreferredSize();
		HTMLPane.reduceHeight(button, textDim.height);

	} // end reducePreferredHeight(JComponent)

	private void wireEvents() {
		this.securityList.addActionListener(this);
		this.fldDecimals.addFocusListener(this);
		this.btnStage.addActionListener(this);
		this.btnCommit.addActionListener(this);

	} // end wireEvents()

	/**
	 * Invoked when an action occurs.
	 *
	 * @param event
	 */
	public void actionPerformed(ActionEvent event) {
		Object source = event.getSource();

		if (source == this.securityList) {
			CurrencyType security = getSecurity();

			if (security != null) {
				setNewDecimals(security.getDecimalPlaces());
				this.btnStage.setEnabled(false);
				this.btnCommit.setEnabled(false);
			}
		}

		if (source == this.btnStage && this.feature != null) {
			this.feature.changeDecimals();
		}

		if (source == this.btnCommit && this.feature != null) {
			this.feature.commitChanges();
		}

	} // end actionPerformed(ActionEvent)

	public void focusGained(FocusEvent event) {
		Object source = event.getSource();

		if (source == this.fldDecimals) {
			if (getSecurity() != null) {
				this.btnStage.setEnabled(true);
			}

			// invoke later because when setValue is called any selection would be lost
			SwingUtilities.invokeLater(new Runnable() {
				public void run() {
					MoreDecimalWindow.this.fldDecimals.selectAll();

				} // end run()
			});
		}

	} // end focusGained(FocusEvent)

	public void focusLost(FocusEvent event) {
		Object source = event.getSource();

		if (source == this.fldDecimals) {
			// can't think of anything to do here
		}

	} // end focusLost(FocusEvent)

	public CurrencyType getSecurity() {

		return (CurrencyType) this.securityList.getSelectedItem();
	} // end getSecurity()

	public int getNewDecimals() {
		Number value = (Number) this.fldDecimals.getValue();

		return value.intValue();
	} // end getNewDecimals()

	private void setNewDecimals(int value) {
		this.fldDecimals.setValue(value);

	} // end setNewDecimals(int)

	/**
	 * @param text HTML text to append to the output log text area
	 */
	public void addText(String text) {
		this.pnOutputLog.addText(text);

	} // end addText(String)

	/**
	 * Clear the output log text area.
	 */
	void clearText() {
		this.pnOutputLog.clearText();

	} // end clearText()

	/**
	 * @param b true to enable the button, otherwise false
	 */
	public void enableCommitButton(boolean b) {
		this.btnCommit.setEnabled(b);

	} // end enableCommitButton(boolean)

	/**
	 * Disable all actions on this window.
	 */
	public void disableActions() {
		this.securityList.setEnabled(false);
		this.fldDecimals.setEnabled(false);
		this.btnStage.setEnabled(false);
		this.btnCommit.setEnabled(false);

	} // end disableActions()

	/**
	 * Processes events on this window.
	 *
	 * @param event
	 */
	protected void processEvent(AWTEvent event) {
		if (event.getID() == WindowEvent.WINDOW_CLOSING) {
			if (this.feature != null) {
				this.feature.closeWindow();
			} else {
				goAway();
			}
		} else {
			super.processEvent(event);
		}

	} // end processEvent(AWTEvent)

	/**
	 * Remove this frame.
	 *
	 * @return null
	 */
	public MoreDecimalWindow goAway() {
		Dimension winSize = getSize();
		System.err.format(getLocale(), "Closing %s with width=%.0f, height=%.0f.%n",
			getTitle(), winSize.getWidth(), winSize.getHeight());
		setVisible(false);
		dispose();

		return null;
	} // end goAway()

} // end class MoreDecimalWindow
