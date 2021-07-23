const bubbleSort = function (arr) {
  // 앞 뒤 요소 비교
  // 앞이 크면 swap이용 위치 바꿈
  // 이 과정 반복 단, 마지막에서 두번쨰 요소와 마지막 요소 비교
  // 이 과정을 통해 가장 큰 요소가 배열의 마지막으로 변경
  // 이 과정 반복해서 오름차순으로 만듬
  // 과정을 배열의 크기 n번 반복하는데...만약 이미 정렬된게 들어온다면 n번 반복 무의미
  // 한번 swap에 들어갔다 왔는데 변한게 없다면 더이상 반복하지 않고 반환이 필요
  // flag를 통해서 정렬이 됬는지 아닌지 확인 후 정렬됬다면 반복을 멈춘다
  let cnt = arr.length;
  while(cnt > 0){
    if(swap(arr)){
      break;
    }
    cnt--;
  }
  return arr;
  
};

function swap(arr){
  let swap = 0;
  let flag = true;
  for(let i = 0; i < arr.length; i++){
    if(i + 1 !== arr.length && arr[i] > arr[i + 1]){
      swap = arr[i];
      arr[i] = arr[i + 1];
      arr[i + 1] = swap;
      flag = false;
    }
  }
  return flag;
}


/*******************************************************************/
// Reference by CodeStates
/******************************************************************/
const swap = function (idx1, idx2, arr) {
  // 두 변수를 바꾸는 방법

  // 1) 임시 변수를 활용한 방법
  // let temp = arr[idx1];
  // arr[idx1] = arr[idx2];
  // arr[idx2] = temp;

  // 2) Destructuring assignment를 활용한 방법
  // arr이 reference type이라 가능
  [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];

  // 3) XOR 연산을 활용한 방법
  // arr이 reference type이라 가능
  // arr[idx1] ^= arr[idx2];
  // arr[idx2] ^= arr[idx1];
  // arr[idx1] ^= arr[idx2];
};

// naive solution
// let bubbleSort = function (arr) {
//   let N = arr.length;

//   for (let i = 0; i < N - 1; i++) {
//     // 매 반복(iteration)마다 i번째로 큰 수가 마지막에서 i번째 위치하게 된다.
//     // 이미 정렬된 요소는 고려할 필요가 없으므로, 'j < N - 1 - i'만 비교하면 된다.
//     for (let j = 0; j < N - 1 - i; j++) {
//       if (arr[j] > arr[j + 1]) {
//         swap(j, j + 1, arr);
//       }
//     }
//   }

//   return arr;
// };

// optimized solution
let bubbleSort = function (arr) {
  let N = arr.length;

  for (let i = 0; i < N; i++) {
    // swap 횟수를 기록한다.
    // 어떤 요소도 swap되지 않은 경우, 배열은 정렬된 상태이다.
    let swaps = 0;

    // 매 반복(iteration)마다 i번째로 큰 수가 마지막에서 i번째 위치하게 된다.
    // 이미 정렬된 요소는 고려할 필요가 없으므로, 'j < N - 1 - i'만 비교하면 된다.
    for (let j = 0; j < N - 1 - i; j++) {
      if (arr[j] > arr[j + 1]) {
        swaps++;
        swap(j, j + 1, arr);
      }
    }

    if (swaps === 0) {
      break;
    }
  }

  return arr;
};
