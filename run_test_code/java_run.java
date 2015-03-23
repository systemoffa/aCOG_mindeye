/*
 by Oliver! :D
 using this helpful tutorial:	http://www.avajava.com/tutorials/lessons/how-do-i-run-another-application-from-java.html
 another tutorial:	http://bytes.com/topic/python/insights/949995-three-ways-run-python-programs-java
*/

import java.io.*;

class aCOG_Start {
	public static void main(String[] args) {
		System.out.println("Yo dawg\n");
		
		//directly from tutorial
		try {
			System.out.println("Opening Pupil");
			Runtime runTime = Runtime.getRuntime();
			
			Process process = runTime.exec("python ~/Desktop/hide/sen 15 (+ winter)/design/nongit_pupil/pupil-0.4.1/pupil_src/capture/main.py");
			/*
			try {
				Thread.sleep(1000000);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			System.out.println("Closing Pupil");
			process.destroy();
			*/
			process.join();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}
}