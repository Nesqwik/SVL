
public class Buffer {
	public int size;
	[Rep] public char[] buff;
	public int idxNextGetElement;
	public int idxNextStoreElement;
	public int nbElement;

	invariant size > 0;
	invariant buff.Length == size;
	invariant idxNextGetElement >= 0 && idxNextGetElement < size;
	invariant idxNextStoreElement >= 0 && idxNextStoreElement < size;
	invariant nbElement >= 0 && nbElement <= size;


	public Buffer(int size)
		requires size > 0;
		ensures nbElement == 0;
		ensures idxNextGetElement == 0;
		ensures idxNextStoreElement == 0;
		ensures size == this.size;
		ensures this.buff != null;
	{
			nbElement = 0;
			idxNextGetElement = 0;
			idxNextStoreElement = 0;
			this.size = size;
			buff = new char[size];
	}

	public char get()
		requires this.buff != null;
		requires idxNextGetElement >= 0 && this.idxNextGetElement < this.buff.Length;
		requires nbElement > 0 && nbElement <= size;
		ensures idxNextGetElement == old(idxNextGetElement) + 1 || idxNextGetElement == 0;
		ensures nbElement == old(nbElement) - 1;
		ensures result == this.buff[old(this.idxNextGetElement)];
	{
		char output = this.buff[idxNextGetElement];
		idxNextGetElement++;
		nbElement--;

		if(idxNextGetElement >= size){
			idxNextGetElement = 0;
		}
		return output;
	}


	public void store(char toStore)
		requires this.buff != null;
		requires idxNextStoreElement >= 0 && this.idxNextStoreElement < this.buff.Length;
		requires nbElement >= 0 && nbElement < size;
		ensures idxNextStoreElement == old(idxNextStoreElement) + 1 || idxNextStoreElement == 0;
		ensures nbElement == old(nbElement) + 1;
	{
		this.buff[idxNextStoreElement] = toStore;
		idxNextStoreElement++;
		nbElement++;
		if(idxNextStoreElement >= size){
			idxNextStoreElement = 0;
		}
	}
}
