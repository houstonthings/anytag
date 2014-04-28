var app = angular.module('ItemListApp');

app.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

app.controller("ItemListController", [$scope, function($scope){
    $scope.list_name = "List 1";
}]);