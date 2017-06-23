
var app = angular.module("asak", ['ngRoute', 'ngResource'])
    .config(function($routeProvider) {
        $routeProvider
            .when('/', {
                controller: "mefakdimCtrl",
                templateUrl: "/media/templates/mefakdim.tpl.html"
            });
    }
);