import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { UserService } from '../user.service';
import { throwError } from 'rxjs';
import jspdf from 'jspdf';
import { jsPDF } from 'jspdf';
@Component({
  selector: 'app-pets',
  templateUrl: './pets.component.html',
  styleUrls: ['./pets.component.scss'],
})
export class PetsComponent implements OnInit {
  public rejestry: any;
  public rejestr: any;
  constructor(private userService: UserService) {}
  error = false;
  getPets() {
    this.userService.list().subscribe(
      (data) => {
        console.log(data[0]);
        this.rejestry = data;
        for (let post of this.rejestry) {
          post.date = new Date(post.date);
        }
      },

      (err) => {
        console.error(err);
        this.error = true;
      }
    );
  }

  createPet() {
    this.userService.create(this.rejestr, this.userService.token).subscribe(
      (data) => {
        this.getPets();
        return true;
      },
      (error) => {
        console.error('Error saving!');
        return throwError(error);
      }
    );
    this.rejestr = {};
  }
  ngOnInit(): void {
    this.getPets();
    this.rejestr = {};
  }
  addGroupToggle() {
    const overlay = document.getElementById('overlay');
    const modal = document.getElementById('modal');
    overlay?.classList.toggle('active');
    modal?.classList.toggle('active');
  }

  open() {
    this.rejestr = {};
    this.addGroupToggle();
  }
  submitForm() {
    this.createPet();
    this.addGroupToggle();
  }
  modify(rej) {
    this.rejestr = rej;
    console.log(this.rejestr);
    this.addGroupToggle();
  }
}
