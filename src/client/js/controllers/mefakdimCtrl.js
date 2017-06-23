
app.controller('mefakdimCtrl', function($scope, Category) {

    Category.get();

    $scope.data = {
        selectedCategory: {}
    };
});