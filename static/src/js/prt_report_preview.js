odoo.define('prt_report_attachment_preview.ReportPreview', function (require) {
"use strict";

var core = require('web.core');
var utils = require('web.utils');
var time = require('web.time');
var ajax = require('web.ajax');
console.log("Ajax");
console.log(ajax);
ajax.include({

  // Get File
  get_file: function(options) {
      var token = new Date().getTime();
      console.log("Options");
      console.log(options);

      var params = _.extend({}, options.data || {}, {token: token});
      var url = options.session.url(options.url, params);
      if (options.complete) { options.complete(); }

      var w = window.open(url);
      if (!w || w.closed || typeof w.closed === 'undefined') {
          // popup was blocked
          return false;
      }
      return true;
    },
 // End
  });
});
