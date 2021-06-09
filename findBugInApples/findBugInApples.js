function findBugInApples(arr) {
  let locateB = [0,0];
  for(let i = 0; i < arr.length; i++){
    for(let j = 0; j < arr[i].length; j++){
      if(arr[i][j] === 'B'){
        locateB[1] = j;
        locateB[0] = i;
        return locateB;
      }
    }
  }
  return locateB;
}

