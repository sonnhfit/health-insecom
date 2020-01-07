var appURL = '';
require.config({
    baseUrl: '/',
	urlArgs: "bust=121",
    waitSeconds: 600,
    paths: {
		'angular'          : 'scripts/components/angular-1.6.6/angular.min',
		'angular-route'    : 'scripts/components/angular-1.6.6/angular-route.min',
  	'angular-cookies'  : 'scripts/components/angular-1.6.6/angular-cookies',
    'angular-animate'  : 'scripts/components/angular-1.6.6/angular-animate.min',
    'angular-aria'     : 'scripts/components/angular-1.6.6/angular-aria.min',
    'angular-material' : 'scripts/components/angular-1.6.6/angular-material.min',
    'angular-messages' : 'scripts/components/angular-1.6.6/angular-messages.min',
    'pikaday-angular'   : 'scripts/components/pikaday/pikaday-angular',
    'pikaday'           : 'scripts/components/pikaday/pikaday',
    'moment'            : 'scripts/components/pikaday/moment',
    'angular-sanitize' : 'scripts/components/angular-1.6.6/angular-sanitize.min',
    'underscore'       : 'scripts/components/underscore/underscore-min',
		'app': appURL+'app'
    },
	shim: {
		'app': {
			deps: ['angular', 'angular-route', 'angular-cookies','angular-animate','angular-aria','angular-material','angular-messages','underscore','pikaday-angular','moment','pikaday','angular-sanitize']
		},
		'angular-route': {
			deps: ['angular']
		},
		'angular-cookies':{
     	deps: ['angular']
    },
    'angular-animate':{
      deps: ['angular']
    },
    'angular-aria':{
      deps: ['angular']
    },
    'angular-material':{
      deps: ['angular','angular-animate','angular-aria']
    },
    'pikaday-angular': {
        deps: ['angular']
    },
    'pikaday': {
      deps: ['angular','pikaday-angular']
    },
    'angular-sanitize' : {
      deps: ['angular']
    },
    'angular-messages':{
      deps: ['angular','angular-animate','angular-aria']
    },
    'underscore':{
      exports: "_",
      deps: ['angular']
    }
	}
});

require
(
    [
        'app'
    ],
    function(app)
    {
        angular.bootstrap(document, ['app']);
    }
);