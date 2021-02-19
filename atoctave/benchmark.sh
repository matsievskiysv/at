#!/usr/bin/env bash

rm -f results

for n in $(seq 1 $(nproc)); do
    for sc in auto runtime dynamic "dynamic, 1" "dynamic, 10" "dynamic, 50" \
		   guided "guided, 1" "guided, 10" "guided, 50" \
		   static "static, 1" "static, 10" "static, 50"; do
	echo "Threads: $n; scheduler: $sc" | tee --append results
	OMP_NUM_THREADS="$n" OMP_SCHEDULE="$sc" octave --eval 'bootstrap;trackMultipleParticles' >> results
    done
done

sed -i '/\/at\//d' results
sed -i -Ez 's/\n[0-9a-z, ]+?, +(with|without) +[0-9a-z, ]+?: +([0-9.]+)[0-9a-z, ]+?/; \1: \2/g' results
echo 'threads,without,with,scheduler,slices' > data.csv
sed -E 's/^[Tt]hreads: +([0-9]+); +scheduler: +([0-9a-zA-Z, ]+); +without: +([0-9.]+); +with: +([0-9.]+)/\1,\3,\4,\2/g' results | sed 's/ //g' >> data.csv
