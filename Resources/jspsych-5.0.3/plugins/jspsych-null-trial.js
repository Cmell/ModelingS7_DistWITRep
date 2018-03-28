jsPsych.plugins['null-trial'] = (function(){

  var plugin = {};

  plugin.trial = function(display_element, trial){
    //setTimeout(jsPsych.finishTrial, 100);
    jsPsych.finishTrial();
  }

  return plugin;

})();
