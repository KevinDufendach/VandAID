(function () {
  'use strict';

  angular
    .module('app.fields')
    .directive('vaSubmitButton', vaSubmitButton);

  /* @ngInject */
  function vaSubmitButton() {
    var directive = {
      bindToController: true,
      controller: submitButtonCtrl,
      controllerAs: 'vm',
      templateUrl: '/app/fields/submitButton.directive.html',
      restrict: 'EA',
      scope: {}
    };
    return directive;

  }

  submitButtonCtrl.$inject = ['vandaidFieldService'];

  function submitButtonCtrl(vandaidFieldService) {
    this.submit = vandaidFieldService.submit;

  }

})();
