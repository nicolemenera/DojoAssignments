    function game(quarter) {
  

    while ( quarter >= 1) {

      var reward = Math.floor(Math.random()*50)+51;
      var chance = Math.floor(Math.random()*100)+1;



      if ( chance === 32 ) {
        quarter = quarter + reward;

        console.log("You have", quarter, "!");
      }
      quarter--;
    }
    console.log(quarter);
    }
  game(30);