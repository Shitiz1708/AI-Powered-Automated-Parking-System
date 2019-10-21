package com.example.sakshigupta.database;



import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class MainActivity extends AppCompatActivity {
    FirebaseDatabase Database;
    DatabaseReference mRef;
    private FirebaseAuth mauth;
    private FirebaseAuth.AuthStateListener authStateListener;
    private EditText emaill;
    private EditText passwordd;
    private Button signup;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        emaill=(EditText)findViewById(R.id.email);
        passwordd=(EditText)findViewById(R.id.pass);
        signup=(Button)findViewById(R.id.SIGNUP);
        mauth=FirebaseAuth.getInstance();

        signup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(MainActivity.this,MapsActivity.class) ;
                startActivity(intent);

            }
        });
        authStateListener = new FirebaseAuth.AuthStateListener() {
            @Override
            public void onAuthStateChanged(@NonNull FirebaseAuth firebaseAuth) {
                if(firebaseAuth.getCurrentUser()!=null){
                    Intent intent =new Intent(MainActivity.this,MapsActivity.class);
                    startActivity(intent);
                }
            }
        };


    }

    public void signinbuttonclicked(View view) {

        String email= emaill.getText().toString();
        String password = passwordd.getText().toString();
        if (TextUtils.isEmpty(email) || TextUtils.isEmpty(password)){
            Toast.makeText(this,"enter both values",Toast.LENGTH_LONG).show();
        }

        else{
            mauth.signInWithEmailAndPassword(email,password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                @Override
                public void onComplete(@NonNull Task<AuthResult> task) {
                    if (!task.isSuccessful()){
                        Toast.makeText(MainActivity.this,"incorrect username or password",Toast.LENGTH_LONG).show();
                    }
                }
            });
        }
    }



}
