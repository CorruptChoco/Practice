function solution(number){
    const multiples = [];
    for (let i = 1; i * 3 < number; i++){
      multiples.push(i * 3);
    }
    for (let i = 1; i * 5 < number; i++){
      multiples.push(i * 5);
    }
    const filterMultiples = multiples.filter((value, index) => multiples.indexOf(value) === index);
    let sum = filterMultiples.reduce((acc, a) => acc + a, 0);
    if (number < 3){
      return 0;
    } else {
      return sum;
    }
  }

  console.log(solution(10))

// alternate better code that was a possible solution
  // function solution(number){
  //   var sum = 0;
    
  //   for(var i = 1;i< number; i++){
  //     if(i % 3 == 0 || i % 5 == 0){
  //       sum += i
  //     }
  //   }
  //   return sum;
  // }