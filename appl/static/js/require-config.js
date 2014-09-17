var require = {
  baseUrl: '/static/js',
  paths: {
    'jquery': 'vendor/jquery.1.11.min',
    'bootstrap': 'vendor/bootstrap.3.1.1.min',
    'bootstrap-datepicker': 'vendor/bootstrap-datepicker',
    'bootstrap-datepicker-zh': 'vendor/bootstrap-datepicker.zh-CN',
    'q': 'vendor/q',
    'lodash': 'vendor/lodash.2.4.1.min',
    'angular': 'vendor/angular.1.2.16.min',
    'angular-bootstrap': './angular-bootstrap',
  },
  shim: {
    'bootstrap': [ 'jquery' ],
    'bootstrap-datepicker': [ 'bootstrap' ],
    'bootstrap-datepicker-zh': [ 'bootstrap-datepicker' ],
    'angular': {
      exports: 'angular'
    }
  },
  deps: [ 'bootstrap' ]
};