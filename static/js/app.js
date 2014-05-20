app = angular.module('anytag.app.static', []);
app.controller('AppController', ['$scope', '$http', function($scope, $http){
    $http.get('/api/items').then(function(result){
        $scope.items = [];
        _.each(result.data, function(item){
            $scope.items.push(item);
        });
        $scope.listparent = $scope.items[0];
    });
}]);