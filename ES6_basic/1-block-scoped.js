export default function taskBlock(trueOrFalse) {
    var task = false;
    var task2 = true;
  
    if (trueOrFalse) {
      var cdtBlockTask = true;
      var cdtBlockTask2 = false;
    }
  
    return [task, task2];
  }
