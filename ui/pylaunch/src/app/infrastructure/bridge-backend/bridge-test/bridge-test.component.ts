import { Component, OnInit } from '@angular/core';
import { from, Observable } from 'rxjs';
import { eel } from '../eel';

@Component({
  selector: 'app-bridge-test',
  templateUrl: './bridge-test.component.html',
  styleUrls: ['./bridge-test.component.css']
})
export class BridgeTestComponent implements OnInit {

  testValue = undefined;
  testSum$ = this.queryTestSumAsync()

  constructor() { }


  ngOnInit(): void {
    eel
    .exec("debug_hello")
    .then((value) => this.testValue = value);

    eel
    .exec("debug_sum", 2, 2)
    .then((value) => console.log(value));

    eel
    .exec("debug_void")
    .then(() => {})
  }

  queryTestSumAsync(): Observable<any> {
    return from(eel.exec("debug_sum", 2, 2));
  }
}
