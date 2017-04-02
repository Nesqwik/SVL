
public class Buffer {
	//@ public invariant size > 0;
	//@ public invariant buff.length == size;
	//@ public invariant idxNextGetElement >= 0 && idxNextGetElement < size;
	//@ public invariant idxNextStoreElement >= 0 && idxNextStoreElement < size;
	//@ public invariant nbElement >= 0 && nbElement <= size;

	public int size;
	public char[] buff;
	public int idxNextGetElement;
	public int idxNextStoreElement;
	public int nbElement;

	//@ requires size > 0;
	//@ ensures nbElement == 0;
	//@ ensures idxNextGetElement == 0;
	//@ ensures idxNextStoreElement == 0;
	//@ ensures size == this.size;
	//@ ensures this.buff != null;
	public Buffer(int size) {
			nbElement = 0;
			idxNextGetElement = 0;
			idxNextStoreElement = 0;
			this.size = size;
			buff = new char[size];
	}

	//@ requires this.buff != null;
	//@ requires idxNextGetElement >= 0 && this.idxNextGetElement < this.buff.length;
	//@ requires nbElement > 0 && nbElement <= size;
	//@ ensures idxNextGetElement == \old(idxNextGetElement) + 1 || idxNextGetElement == 0;
	//@ ensures nbElement == \old(nbElement) - 1;
	//@ ensures \result == this.buff[\old(this.idxNextGetElement)];
	public char get(){
		char output = this.buff[idxNextGetElement];
		idxNextGetElement++;
		nbElement--;

		if(idxNextGetElement >= size){
			idxNextGetElement = 0;
		}
		return output;
	}


	//@ requires this.buff != null;
	//@ requires idxNextStoreElement >= 0 && this.idxNextStoreElement < this.buff.length;
	//@ requires nbElement >= 0 && nbElement < size;
	//@ ensures idxNextStoreElement == \old(idxNextStoreElement) + 1 || idxNextStoreElement == 0;
	//@ ensures nbElement == \old(nbElement) + 1;
	public void store(char toStore){
		this.buff[idxNextStoreElement] = toStore;
		idxNextStoreElement++;
		nbElement++;
		if(idxNextStoreElement >= size){
			idxNextStoreElement = 0;
		}
	}
}
