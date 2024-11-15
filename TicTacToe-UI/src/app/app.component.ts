import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {TicTacToeComponent} from './tic-tac-toe/tic-tac-toe.component'
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,TicTacToeComponent,CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'TicTacToe-UI';
  isVisible = true;
}
