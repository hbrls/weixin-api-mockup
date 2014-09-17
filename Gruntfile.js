module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    sass: {
      dist: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          'appl/static/css/style.css': 'appl/static/sass/style.scss'
        }
      }
    },
    jshint: {
      options: {
        ignores: [
          'appl/static/js/vendor/*.js'
        ]
      },
      all: [
        'Gruntfile.js',
        'appl/static/js/**/*.js'
      ]
    },
  });

  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-jshint');

  grunt.registerTask('build', [ 'sass' ]);
  grunt.registerTask('test', [ 'jshint' ]);
};