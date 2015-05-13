def deleteFile(self, tfile):
        if printOps:
            print 'unlink("%s");' % tfile

        inum = self.nameToInum[tfile]
        if self.inodes[inum].refCnt == 1:
            self.dataFree(inum)
            self.inodeFree(inum)
        else:
        	self.inodes[inum].decRefCnt()
        parent = getParent(tfile)
        num = self.nameToInum(parent)
        self.inodes[num].decRefCnt()
        self.data[num].delDirEntry(tfile)
    # YOUR CODE, YOUR ID
        # IF inode.refcnt ==1, THEN free data blocks first, then free inode, ELSE dec indoe.refcnt
        # remove from parent directory: delete from parent inum, delete from parent addr
    # DONE

        # finally, remove from files list
        self.files.remove(tfile)
        return 0

    def createLink(self, target, newfile, parent):
    # YOUR CODE, YOUR ID
        # find info about parent
        # is there room in the parent directory?
        # if the newfile was already in parent dir?
        # now, find inumber of target
        # inc parent ref count
        # now add to directory
    # DONE
        num = self.nameToInum(parent)
        paddr = self.inodes[num].getAddr()
        if self.data[paddr].dirEntryExists(newfile) == true:
            print 'not exist'
            return -1;
         tinum = self.nameToInum(target)
         self.inodes[num].incRefCnt()
         self.inodes[t_num].incRefCnt()
        return tinum

    def createFile(self, parent, newfile, ftype):
    # YOUR CODE, YOUR ID
        # find info about parent
        # is there room in the parent directory?
        # have to make sure file name is unique
        # find free inode
        # if a directory, have to allocate directory block for basic (., ..) info
        # now ok to init inode properly
        # inc parent ref count
        # and add to directory of parent
    # DONE
        parent = self.nameToInum(parent)
        paddr = self.inodes[parent].getAddr()
        if self.data[paddr].dirEntryExists(newfile) == true:
        	return -1
        if(self.data[paddr].getFreeEntries() <= 0):
        	return -1
        daddr = self.dbitmap.alloc()
        iaddr = self.ibitmap.alloc()
        self.data[paddr].addDirEntry(newfile,daddr)
        if ftype == 'd':
        	self.inodes[iaddr].setAll('d',paddr,2)
        	self.data[daddr].setType('d')
        	self.data[daddr].addDirEntry('.',daddr)
        	self.data[daddr].addDirEntry('..',paddr)
       else:
       	self.inodes[iaddr].setAll('f',-1,1)
       self.inodes[paddr].incRefCnt()
       return inum

    def writeFile(self, tfile, data):
        inum = self.nameToInum[tfile]
        curSize = self.inodes[inum].getSize()
        dprint('writeFile: inum:%d cursize:%d refcnt:%d' % (inum, curSize, self.inodes[inum].getRefCnt()))
        if curSize != 0:
        	return -1
        daddr =  self.dbitmap.alloc()
        if daddr != -1:
        	self.data[daddr].setType('f')
        	self.data[daddr].addData(data)
        else:
        	return -1
    # YOUR CODE, YOUR ID
        # file is full?
        # no data blocks left
        # write file data
    # DONE
