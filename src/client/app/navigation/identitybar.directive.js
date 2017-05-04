(function() {
  'use strict';

  angular
    .module('app.nav')
    .directive('vandaidIdentityBar', IdentityBar);

  function IdentityBar() {
    var directive = {
      restrict: 'E',
      templateUrl: '/app/navigation/identitybar.directive.html',
      scope: { },
      controller: IdentityBarController,
      controllerAs: 'vm'
    };
    return directive;
  }

  IdentityBarController.$inject = ['vandaidUserService', '$mdSidenav', '__va', '$scope'];

  function IdentityBarController(vandaidUserService, $mdSidenav, __va, $scope) {
    var vm = this;

    vm.toggleSidenav = toggleSidenav;
    vm.isLoggedIn = vandaidUserService.isLoggedIn();
    vm.getLogo = getLogo;
    vm.getBackground = getBackground;

    //////////////

    function toggleSidenav(navID) {
      $mdSidenav(navID).toggle();
    }

    function getLogo() {
      return __va.logo || 'content/img/Vanderbilt-Logo-white500x500.png';
    }

    function getBackground() {
      return __va.logoBackground || 'rgb(153,127,61)';
    }
  }

})();