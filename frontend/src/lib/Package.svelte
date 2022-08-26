<script lang="ts">
	import DependencyGrid from '$lib/DependencyGrid.svelte';

	interface Constraint {
		version_constraint: string;
	}

	interface Dependency {
		name: string;
	}

	type DependencyTuple = [Dependency, Constraint];

	interface Package {
		name: string;
		status: string;
		maintainer: string;
		version: string;
		description: string;
		depends?: DependencyTuple[];
		reverse_depends?: DependencyTuple[];
		alts?: DependencyTuple[];
		conflicts?: DependencyTuple[];
		suggests?: string[];
		priority?: string;
		section?: string;
		installed_size?: number;
		architecture?: string;
		homepage?: string;
	}

	export let details: Package;

	console.log(details);
</script>

<div class="max-w-7xl mx-auto px-4 my-4 sm:px-6 md:px-8 flex">
	<h1 class="text-3xl font-medium text-gray-900">{details.name}</h1>
	<span class="ml-5 inline-flex items-center px-3 py-0.5 rounded-full text-lg font-medium bg-green-200 text-green-900">{details.version}</span>
</div>
<div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
	<DependencyGrid title="Dependencies" dependencies={details.depends} />

	<DependencyGrid title="Reverse Dependencies" dependencies={details.reverse_depends} />

	<div class="py-4 rounded-lg border border-gray-300 bg-white shadow-sm px-10">
		<div class="my-5">
			<h2 class="text-lg font-medium text-gray-800">Description</h2>

			<div class="mt-4 text-gray-600">
				<p class="whitespace-pre-line">
					{details.description}
				</p>
			</div>
		</div>
	</div>
</div>
