using System;
using System.Diagnostics.Contracts;

public class Buffer {
	public int size;
	public char[] buff;
	public int idxNextGetElement;
	public int idxNextStoreElement;
	public int nbElement;

	[ContractInvariantMethod]
	void ObjectInvariant () {
			Contract.Invariant(this.size > 0);
			Contract.Invariant(this.buff.Length == size);
			Contract.Invariant(this.idxNextGetElement >= 0 && this.idxNextGetElement < this.size);
			Contract.Invariant(this.idxNextStoreElement >= 0 && this.idxNextStoreElement < this.size);
			Contract.Invariant(this.nbElement >= 0 && this.nbElement <= size);
  }

	public Buffer(int size) {
			Contract.Requires(size > 0);
			Contract.Ensures(nbElement == 0);
			Contract.Ensures(idxNextGetElement == 0);
			Contract.Ensures(idxNextGetElement == 0);
			Contract.Ensures(size == this.size);
			Contract.Ensures(this.buff != null);
			nbElement = 0;
			idxNextGetElement = 0;
			idxNextStoreElement = 0;
			this.size = size;
			buff = new char[size];
	}

	public char get(){
		Contract.Requires(this.buff != null);
		Contract.Requires(idxNextGetElement >= 0 && this.idxNextGetElement < this.buff.Length);
		Contract.Requires(nbElement > 0 && nbElement <= size);
		Contract.Ensures(idxNextGetElement == Contract.OldValue(idxNextGetElement) + 1 || idxNextGetElement == 0);
		Contract.Ensures(nbElement == Contract.OldValue(nbElement) - 1);
		Contract.Ensures(Contract.Result<char>() == this.buff[Contract.OldValue(this.idxNextGetElement)]);

		char output = this.buff[idxNextGetElement];
		idxNextGetElement++;
		nbElement--;

		if(idxNextGetElement >= size){
			idxNextGetElement = 0;
		}
		return output;
	}

	public void store(char toStore){
		Contract.Requires(this.buff != null);
		Contract.Requires(idxNextStoreElement >= 0 && this.idxNextStoreElement < this.buff.Length);
		Contract.Requires(nbElement >= 0 && nbElement < size);
		Contract.Ensures(idxNextStoreElement == Contract.OldValue(idxNextStoreElement) + 1 || idxNextStoreElement == 0);
		Contract.Ensures(nbElement == Contract.OldValue(nbElement) + 1);

		this.buff[idxNextStoreElement] = toStore;
		idxNextStoreElement++;
		nbElement++;
		if(idxNextStoreElement >= size){
			idxNextStoreElement = 0;
		}
	}
}
