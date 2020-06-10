for d in ~/Documents/yearwisedataset/*/*/; do
	if [ -d "$d" ]; then
	  cd $d
	  BASENAME=`basename "$PWD"`
	  cat *.csv > ${BASENAME}.csv
	  ls | grep -v ${BASENAME}.csv | parallel rm
	fi
done

