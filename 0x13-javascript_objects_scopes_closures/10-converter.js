#!/usr/bin/node

exports.converter = function (base) {
  // Define a recursive function to convert a number to the specified base
  const convertToBase = function (number) {
    const hexDigits = '0123456789abcdef';

    if (number < base) {
      // B: if the number is less than the base
      return hexDigits[number];
    } else {
      // Recursive: convert the quotient and append the remainder as a hex digit
      return convertToBase(Math.floor(number / base)) + hexDigits[number % base];
    }
  };

  // Return the inner function for external use
  return convertToBase;
};
