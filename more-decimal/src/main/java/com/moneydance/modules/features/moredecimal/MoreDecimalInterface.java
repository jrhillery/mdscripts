/*
 * Created on May 10, 2020
 */
package com.moneydance.modules.features.moredecimal;

import java.util.Locale;

/**
 * Interface the more decimal processor uses to interact with its window.
 */
public interface MoreDecimalInterface {

	/**
	 * @param text HTML text to append to the output log text area
	 */
	void addText(String text);

	/**
	 * @return The Locale object that is associated with this window
	 */
	Locale getLocale();

} // end interface MoreDecimalInterface
