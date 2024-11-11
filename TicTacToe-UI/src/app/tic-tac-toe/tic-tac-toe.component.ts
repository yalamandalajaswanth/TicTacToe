import { Component } from '@angular/core';

@Component({
  selector: 'app-tic-tac-toe',
  standalone: true,
  imports: [],
  templateUrl: './tic-tac-toe.component.html',
  styleUrl: './tic-tac-toe.component.css'
})
export class TicTacToeComponent {
grid:any = {1:'',
  2:'',
  3:'',
  4:'',
  5:'',
  6:'',
  7:'',
  8:'',
  9:''
}
currentTheme = 'Theme1';
toggleValue(id:string){

  if(this.grid[id] == 'X') this.grid[id] = ''
  else this.grid[id] = 'X'
}
toggleTheme(){
  const element = document.getElementsByClassName('Theme1');
  console.log(element)
  /*
  elements.forEach(element => {
    element.classList.remove(this.currentTheme); 
    if(this.currentTheme === "Theme1"){
      this.currentTheme = "Theme2"
    }
    else{
      this.currentTheme = "Theme1"
    }
    element.classList.add(this.currentTheme);
  });
  */
}
}
