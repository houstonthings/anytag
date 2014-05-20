app = angular.module('anytag.app.static', []);
app.controller('AppController', ['$scope', '$http', function($scope, $http){
    $http.get('/api/tags/').then(function(result){
        $scope.tags = [];
        _.each(result.data, function(val){
            $scope.tags.push(val);
        });
    });
    $http.get('/api/items/').then(function(result){
        $scope.items = [];
        _.each(result.data, function(val){
            $scope.items.push(val);
        });
    });
    $http.get('/api/tagvalues/').then(function(result){
        $scope.tagvalues = [];
        _.each(result.data, function(val){
            $scope.tagvalues.push(val);
        });
    });
}]);