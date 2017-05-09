(function () {
  'use strict';

  angular
    .module('va.canvas')
    .directive('vandaidPaper', vandaidPaper);

  /* @ngInject */
  function vandaidPaper() {
    var directive = {
      replace: true,
      transclude: true,
      restrict: 'E',
      templateUrl: '/src/client/vandaid/canvas/paper.directive.html',
      scope: false
    };
    return directive;
  }

})();

