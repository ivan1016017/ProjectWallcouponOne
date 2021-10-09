/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { VendorSigninComponent } from './vendor-signin.component';

describe('VendorSigninComponent', () => {
  let component: VendorSigninComponent;
  let fixture: ComponentFixture<VendorSigninComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VendorSigninComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VendorSigninComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
