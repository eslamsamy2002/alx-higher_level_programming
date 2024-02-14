#!/usr/bin/node
exports.converter = function (base) {
   function (decimal) {
    return decimal.toString(base);
  };
};
