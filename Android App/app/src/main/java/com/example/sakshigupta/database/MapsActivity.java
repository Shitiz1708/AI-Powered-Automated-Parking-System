package com.example.sakshigupta.database;

import  android.os.Handler;
import android.content.Intent;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;

import com.google.android.gms.maps.CameraUpdate;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptor;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

import java.util.HashMap;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    private Marker MARKER1;
    HashMap<String, String> markerMap = new HashMap<String, String>();
    boolean doubleBackToExitPressedOnce = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);

    }


    /**
     * Manipulates the map once available.
     * This callback is triggered when the map is ready to be used.
     * This is where we can add markers or lines, add listeners or move the camera. In this case,
     * we just add a marker near Sydney, Australia.
     * If Google Play services is not installed on the device, the user will be prompted to install
     * it inside the SupportMapFragment. This method will only be triggered once the user has
     * installed Google Play services and returned to the app.
     */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        mMap.setOnInfoWindowClickListener(new GoogleMap.OnInfoWindowClickListener()
        {

            @Override
            public void onInfoWindowClick(Marker arg0) {
                if(arg0 != null && arg0.getTitle().equals("red fort parking")){
                    Intent intent1 = new Intent(MapsActivity.this, data.class);
                    startActivity(intent1);}

                if(arg0 != null && arg0.getTitle().equals("jama masjid parking")){
                    Intent intent2 = new Intent(MapsActivity.this, data.class);
                    startActivity(intent2);}

                if(arg0 != null && arg0.getTitle().equals("parade ground ")){
                    Intent intent3 = new Intent(MapsActivity.this, data.class);
                    startActivity(intent3);}

                if(arg0 != null && arg0.getTitle().equals("GPO PARKING")){
                    Intent intent4 = new Intent(MapsActivity.this, data.class);
                    startActivity(intent4);}
            }
        });











        // Add a marker in Sydney and move the camera
        LatLng redfort = new LatLng(28.651889, 77.242288);
       MARKER1= mMap.addMarker(new MarkerOptions().position(redfort).title("red fort parking").icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_ORANGE)));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(redfort));


        LatLng jamamasjid = new LatLng(28.652109, 77.235062);
        mMap.addMarker(new MarkerOptions().position(jamamasjid).title("jama masjid parking").icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_BLUE)));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(jamamasjid));

        LatLng paradeground = new LatLng(28.652025, 77.231411);
        mMap.addMarker(new MarkerOptions().position(paradeground).title("parade ground ").icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_MAGENTA)));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(paradeground));

        LatLng gpo = new LatLng(28.661914, 77.235233);
        mMap.addMarker(new MarkerOptions().position(gpo).title("GPO PARKING").icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_YELLOW)));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(gpo));
        CameraUpdate zoom = CameraUpdateFactory.zoomTo(11);
        mMap.moveCamera(zoom);
        mMap.animateCamera(zoom);


    }


}
