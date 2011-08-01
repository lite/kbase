Bitmap and Out of memory
====

http://stackoverflow.com/questions/6632140/android-pixel-quality-reduction-in-images-loaded-in-webview
http://www.apkbus.com/forum.php?mod=viewthread&tid=627

HashMap dataCache

    public View getView(int position, View convertView, ViewGroup parent) {

    if(convertView==null){
    LayoutInflater inflater = LayoutInflater.from(context);
    convertView = inflater.inflate(R.layout.photo_item, null);

    holder = new ViewHolder();
    holder.photo = (ImageView) convertView.findViewById(R.id.photo_item_image);
    holder.photoTitle = (TextView) convertView.findViewById(R.id.photo_item_title);
    holder.photoDate = (TextView) convertView.findViewById(R.id.photo_item_date);
    convertView.setTag(holder);
    }else {
    holder = (ViewHolder) convertView.getTag();
    }
    cursor.moveToPosition(position);

    Bitmap current = dateCache.get(position);
    if(current != null){//如果缓存中已解码该图片，则直接返回缓存中的图片
    holder.photo.setImageBitmap(current);
    }else {
    current = bitmapDecoder.getPhotoItem(cursor.getString(1), 2) ;
    holder.photo.setImageBitmap(current);
    dateCache.put(position, current);
    }
    holder.photoTitle.setText(cursor.getString(2));
    holder.photoDate.setText(cursor.getString(4));
    return convertView;
    }

    }

itmapDecoder.class

    package eoe.wuyi.bestjoy;

    import java.io.FileNotFoundException;
    import java.io.FileOutputStream;

    import android.content.Context;
    import android.graphics.Bitmap;
    import android.graphics.BitmapFactory;
    import android.graphics.Matrix;

    public class BitmapDecoder {
    private static final String TAG = "BitmapDecoder";
    private Context context;
    public BitmapDecoder(Context context) {
    this.context = context;
    }

    public Bitmap getPhotoItem(String filepath,int size) {
    BitmapFactory.Options options = new BitmapFactory.Options();
    options.inSampleSize=size;
    Bitmap bitmap = BitmapFactory.decodeFile(filepath,options);
    bitmap=Bitmap.createScaledBitmap(bitmap, 180, 251, true);
    return bitmap;

    }
    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position,long id) {

    releaseBitmap();
    Log.v(TAG, "select id:"+ id);
    }

    private void releaseBitmap(){
    int start = mGallery.getFirstVisiblePosition()-3;
    int end = mGallery.getLastVisiblePosition()+3;
    Log.v(TAG, "start:"+ start);
    Log.v(TAG, "end:"+ end);
    Bitmap delBitmap;
    for(int del=0;del<start;del++){
    delBitmap = dateCache.get(del);
    if(delBitmap != null){
    Log.v(TAG, "release position:"+ del);
    dateCache.remove(del);
    delBitmap.recycle();
    }
    }

    freeBitmapFromIndex(end);

    }

    private void freeBitmapFromIndex(int end) {
    Bitmap delBitmap;
    for(int del =end+1;del<dateCache.size();del++){
    delBitmap = dateCache.get(del);
    if(delBitmap != null){
    dateCache.remove(del);
    delBitmap.recycle();
    Log.v(TAG, "release position:"+ del);
    }

    }
    }