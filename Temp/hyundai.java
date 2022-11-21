BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
/*
		List<Integer> inputArr = Arrays.stream(input.split(""))
				.map(Integer::parseInt)
				.collect(Collectors.toList());
		int distance = Integer.MAX_VALUE; //거리가 최소
		int sum = Integer.MAX_VALUE; //합이 최소
		List<Integer> result = new ArrayList<>();

		int start = 0;
		int end = 1;

		while (true) {
			try {
				if (Math.abs(inputArr.get(start) - inputArr.get(end)) <= distance) {
					if (inputArr.get(start) + inputArr.get(end) < sum) {
						sum = inputArr.get(start) + inputArr.get(end);
						result.clear();
						result.add(inputArr.get(start));
						result.add(inputArr.get(end));
					}
				}
				if (end < inputArr.size() - 1) {end++;}
				else {
					start++;
					end = start + 1;
				}

			} catch (Exception e) {
				break;
			}
		}

		System.out.println(result.get(0).toString() +" "+ result.get(1).toString());
	}
*/
		List<Integer> inputArr = Arrays.stream(input.split(""))
				.map(Integer::parseInt)
				.collect(Collectors.toList());
		int start = 0;
		int end = inputArr.size();

		List<Integer> toFind = Arrays.stream(input.split(""))
				.map(Integer::parseInt)
				.collect(Collectors.toList());
		int index = 0; //toFind의 인덱스
		int count = 0; //총 횟수
		int left = 0, right = 0;

		List<Integer> indexToFind = new ArrayList<>();
		for (int i = 0; i < inputArr.size(); i++) {
			if (toFind.contains(inputArr.get(i))) {
				indexToFind.add(toFind.indexOf(inputArr.get(i)), i);
			}

			if(index < toFind.size()) break;
		}
