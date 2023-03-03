public void jam_loop() {
    Thread p = new Thread() {
        public void run() {
            for(;;) {

                Calendar cal = new GregorianCalendar();
                int hari = cal.get(Calendar.DAY_OF_MONTH);
                int bulan = cal.get(Calendar.MONTH);
                int tahun = cal.get(Calendar.YEAR);
                tgl.setText(hari + "/" + (bulan + 1) + "/" + tahun);

                int jam = cal.get(Calendar.HOUR);
                int menit = cal.get(Calendar.MINUTE);
                int detik = cal.get(Calendar.SECOND);
                int AM_PM = cal.get(Calendar.AM_PM);

                String day_night = "";

                if (AM_PM == 1) {
                    day_night = "PM";
                } else {
                    day_night = "AM";
                }

                String waktuu = jam + ":" + menit + ":" + detik + " " + day_night;
                
                vakut.setText(waktuu);

                try {
                    sleep(1000);
                } catch (InterruptedException ex) {
                    System.out.println(ex);
                }
            }
        }
    }
    p.start();
}