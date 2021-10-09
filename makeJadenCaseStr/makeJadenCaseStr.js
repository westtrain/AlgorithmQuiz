function solution(s) {
    let answer = '';
    const words = s.toLowerCase().split('');
    let isSpace = true;
    for(let word of words){
        answer += isSpace ? word[0].toUpperCase() : word;
        isSpace = word === ' ' ? true : false;
    }
    
    // let temp = s.toLowerCase();
    // let answer = temp[0].toUpperCase();
    // for(let i = 1; i < temp.length; i++){
    //     if(temp[i] === ' ' && typeof temp[i + 1] === 'string'){
    //         answer += temp[i];
    //         answer += temp[i + 1].toUpperCase();
    //         i++;
    //     }else{
    //         answer += temp[i];
    //     }
    // }
    
    // let answer = s[0].toUpperCase();
    // for(let i = 1; i < s.length; i++){
    //     if(s.charCodeAt(i) === 32){
    //         answer += s[i];
    //         answer += s[i + 1].toUpperCase();
    //         i++;
    //     }else if(s.charCodeAt(i) >= 65 && s.charCodeAt(i) <= 90){
    //         answer += s[i].toLowerCase();
    //     }else{
    //         answer += s[i];
    //     }
    // }
    
    // let answer = s[0].toUpperCase();
    // for(let i = 1; i < s.length; i++){
    //     if(s[i] === ' ' && typeof s[i + 1] === 'string'){
    //         answer += ' ';
    //         answer += s[i + 1].toUpperCase();
    //         i++;
    //     }else{
    //         answer += s[i].toLowerCase();
    //     }
    // }
    
    // let answer = '';
    // const words = s.toLowerCase().split(' ');
    // for(let i = 0; i < words.length; i++){
    //     if(words[i].length === 0){
    //         answer += words[i];
    //     }else{
    //         if(i !== 0){
    //             answer += ' ';
    //         }
    //         answer += words[i][0].toUpperCase();
    //         if(words[i].length >= 2){
    //             answer += words[i].slice(1, words[i].length);        
    //         }   
    //     }
    // }
    return answer;
}

// 문자열의 시작은 대문자로 바꾸고 나머지는 소문자로 바꾸어 반환
// split으로 나누어 문자들을 배열에 넣고
// 각 문자의 첫번째 인덱스에 대문자로 바꾼다
// 나머지 문자들은 모두 소문자로 바꾼다
// 다시 배열속의 문자열들을 순서대로 한 문자열로 바꾸고 반환.
