values = {
    const stream = new Float32Array(nverts);
    const cp = new Float32Array(nverts)
    let k = 0;
    for (let k = 0; k < nverts; k++) {
      let x = initialGrid.grid[2*k];
      let y = initialGrid.grid[2*k+1];
      let z = math.complex(x,y);
      let emialpha = math.exp( math.complex( 0, -alpha) );
      let epialpha = math.exp( math.complex( 0, alpha) );
      let zplusac = math.add( z, c );
      let F1 = math.multiply( zplusac, emialpha );
      let F2 = math.multiply( math.divide( math.complex( (1+c)**2 ,0), zplusac ), epialpha );
      let F3 = math.multiply( math.divide( math.complex( 0, -Gamma), 2*Math.PI ), math.log( zplusac ));
      let F = math.add( F1, F2, F3 );
      stream[k] = F.im;
      let dFdz = math.add( emialpha, math.multiply( math.multiply( math.divide( (1+c), zplusac ), math.divide( (1+c), zplusac )), math.multiply( -1, epialpha )), math.divide( math.complex( 0, -Gamma/(2.*math.PI) ), zplusac) );
      let u = dFdz.re;
      let v = -dFdz.im;
      cp[k] = 1 - (u*u + v*v);
    }
    return {stream, cp};
  }

  initialGrid = {
    const grid = new Float32Array(nverts*2);  // [x0,y0,x1,y1, ....]
    const iVal = new Float32Array(nverts);    // for grid line plotting
    const jVal = new Float32Array(nverts);    // for grid line plotting
    const spac = new Array(nj);
    const dist = new Array(nj);
    
    spac[0] = 1.;
    dist[0] = 0.;
    for ( let j = 1; j < nj; j++ ) {
      spac[j] = spac[j-1]*1.2;                 // spacing of cells radially follows geometric series
      if ( spac[j] > 50. ) { spac[j] = 50.; }
      dist[j] = dist[j-1] + spac[j];
    }
    let ratio = 10. / dist[nj-1];  
    let kGrid = 0;
    let kVert = 0;
    for ( let j = 0; j < nj; j++ ) {
      for ( let i = 0; i < ni; i++ ) {
        let theta = i * 2*Math.PI / (ni-1);
        let r = (1+c) + ratio*dist[j]
        grid[kGrid] = r*Math.cos(theta) - c;
        grid[kGrid+1] = r*Math.sin(theta);
        kGrid += 2;
        iVal[kVert] = i;
        jVal[kVert] = j;
        kVert += 1;
      }
    }
    return {grid, iVal, jVal};
  }