const isSubsetOf = function (base, sample) {
  // TODO: 여기에 코드를 작성합니다.
  // base와 sample에 각각 배열이 입력되는데 base에 sample의 배열 요소들이 부분집합인지 확인
  // 부분 집합이라는 것은 sample의 요소가 base의 배열안에 모두 있다는 뜻
  // 일단은.....단순하게 하면...포문을 두개돌려서 sample의 요소가 base에 있는지 하나씩 확인한다
  // 이때 단 하나라도 존재하지 않으면 false 반환
  // for(let el of sample){
  //   for(let i  = 0; i < base.length; i++){
  //     if(el === base[i]){
  //       break;
  //     }else if(i + 1 === base.length){
  //       return false;
  //     }
  //   }
  // }
  // return true;
  // 위의 방법은....시간 복잡도상 최악인듯...실행시간을 초과함...
  // for(let el of sample){
  //   if(!base.includes(el)){
  //     return false;
  //   }
  // }
  // return true;
  // includes메소드도....포문 돌리는 방식인듯.....실행시간 초과됨...
  // 어떻게 해야하나...
  // 단 하나라도 없으면 거짓인데...그 단 하나의 케이스를 찾는 법..그것도 빠르게...
  // 길이를 재서 샘플이 베이스보다 길면 무조건 거짓 아니면 포문돌리자...
  // if(sample.length > base.length){
  //   return false;
  // }
  // for(let el of sample){
  //   if(!base.includes(el)){
  //     return false;
  //   }
  // }
  // return true;
  // 차이가 없다...아무래도 길이보다 포문을 두개돌리는게 문제인듯....
  // 반복문을 안돌리거나...적어도 한번만 사용하는 법을 찾아야한다....
  // 길이를 비교해서 포문을 긴 쪽에 맞춰 돌리고 객체를 만들어 넣는다
  // 키값에 true를 주는데 만약 이미 있는 키이고 true면 false리턴
  let obj = {}, len = 0;
  for(let i = 0; i < base.length; i++){
    obj[base[i]] = true;
  }
  for(let el of sample){
    if(!(el in obj)){
      return false;
    }
  }
  return true;
};

/* Reference */
/**********************
const isSubsetOf = function (base, sample) {
  // naive solution: O(M * N)
  // return sample.every((item) => base.includes(item));

  // 각 배열을 정렬: O(N * logN), O(M * logM)
  // N >= M 이므로, O(N * logN)
  base.sort((a, b) => a - b);
  sample.sort((a, b) => a - b);

  const findItemInSortedArr = (item, arr, from) => {
    for (let i = from; i < arr.length; i++) {
      if (item === arr[i]) return i;
      else if (item < arr[i]) return -1;
    }
    return -1;
  };

  let baseIdx = 0;
  for (let i = 0; i < sample.length; i++) {
    baseIdx = findItemInSortedArr(sample[i], base, baseIdx);
    if (baseIdx === -1) return false;
  }
  return true;
};
***********************/
