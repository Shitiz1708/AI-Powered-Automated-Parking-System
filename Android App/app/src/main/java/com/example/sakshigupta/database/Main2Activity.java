package com.example.sakshigupta.database;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class Main2Activity extends AppCompatActivity {
    FirebaseDatabase Database;
    DatabaseReference myRef;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        Database= FirebaseDatabase.getInstance();
    }

    public void buttonclicked(View view) {

         EditText number = (EditText) findViewById(R.id.editText);
         EditText time = (EditText) findViewById(R.id.editText2);
         Intent intent5= new Intent(Main2Activity.this, tpt.class);
         startActivity(intent5);}




    }

