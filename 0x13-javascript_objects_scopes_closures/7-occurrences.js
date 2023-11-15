#!/usr/bin/node
//  return the number of occurances of a search element

exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }

  return (count);
};
