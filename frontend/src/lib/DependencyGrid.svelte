<script>
	export let dependencies;

	export let title = 'Dependencies';
</script>

{#if dependencies && dependencies.length > 0}
	<div class="py-4 mb-4">
		<h2 class="text-lg font-medium text-gray-800">{title}</h2>
		<div class="grid grid-cols-1 gap-4 sm:grid-cols-2 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 mt-3">
			{#each dependencies as dep}
				<div
					class="relative rounded-lg border border-gray-300 bg-white px-6 py-5 shadow-sm flex items-center space-x-3 hover:border-gray-400 focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500"
				>
					<div class="flex-1 min-w-0">
						<a href={`/package/${dep[0].name}`} class="focus:outline-none">
							<span class="absolute inset-0" aria-hidden="true" />
							<p class="text-sm font-medium text-gray-900">{dep[0].name}</p>
							{#if dep[1]}<p class="text-sm text-gray-500 truncate">{dep[1]?.version_constraint}</p>{/if}
						</a>
					</div>
				</div>
			{/each}
		</div>
	</div>
{/if}
