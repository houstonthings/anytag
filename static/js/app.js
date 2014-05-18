app = angular.module('example.app.static', []);

app.controller('AppController', ['$scope', '$http', function($scope, $http){
    $http.get('/api/items').then(function(result){
        _.each(result.data, function(item){
            $scope.items.push(item);
        });
    });
}]);
