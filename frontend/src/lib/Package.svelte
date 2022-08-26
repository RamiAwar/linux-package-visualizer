<script lang="ts">
	import DependencyGrid from '$lib/DependencyGrid.svelte';
	import PackageMetadata from '$lib/PackageMetadata.svelte';
	import type { Package } from '$lib/package';

	export let details: Package;

	console.log(details);
</script>

<div class="max-w-7xl mx-auto px-4 my-4 sm:px-6 md:px-8 flex">
	<h1 class="text-3xl font-medium text-gray-900">{details.name}</h1>
	<span class="ml-5 inline-flex items-center px-3 py-0.5 rounded-full text-lg font-medium bg-green-200 text-green-900">{details.version}</span>
</div>
<div class="max-w-7xl mx-auto px-4 sm:px-6 md:px-8">
	<!-- Package info -->
	<PackageMetadata {details} />

	<!-- DEPENDENCIES -->
	<DependencyGrid title="Dependencies" dependencies={details.depends} />
	<DependencyGrid title="Reverse Dependencies" dependencies={details.reverse_depends} />
	<DependencyGrid title="Alternatives" dependencies={details.alts} />

	<!-- DESCRIPTION -->
	<div class="py-4 rounded-lg border border-gray-300 bg-white shadow-sm px-10 max-w-xl">
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
