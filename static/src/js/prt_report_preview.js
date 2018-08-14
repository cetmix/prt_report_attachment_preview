odoo.define('prt_report_attachment_preview.ReportPreview', function (require) {
"use strict";

var Session = require('web.Session');

// session
Session.include({

    get_file: function(options) {
      var token = new Date().getTime();
      options.session = this;
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
  });

});
