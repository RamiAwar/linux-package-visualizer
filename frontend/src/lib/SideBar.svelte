<script>
	export let packages;

	import { page } from '$app/stores';
	$: pageName = $page.url.pathname.substring($page.url.pathname.lastIndexOf('/') + 1);
</script>

<div class="flex w-64 flex-col fixed inset-y-0">
	<a href="/"><div class="py-5 px-3 font-medium text-xl border-r border-b border-gray-200 bg-white">Installed Packages</div></a>
	<div class="flex-1 flex flex-col min-h-0 border-r border-gray-200 bg-white">
		<div id="sidebar" class="flex-1 flex flex-col pb-4 overflow-y-auto">
			<nav class="space-y-1" aria-label="Sidebar">
				{#each packages as pkg (pkg)}
					<a
						href={`/package/${pkg}`}
						sveltekit:noscroll
						class="transition-colors duration-300 flex items-center mx-3 px-3 py-2 text-sm font-normal rounded-md"
						class:current={pageName === pkg}
						aria-current="page"
					>
						{pkg}
					</a>
				{/each}
			</nav>
		</div>
	</div>
</div>

<style>
	.current {
		@apply bg-gray-200 text-gray-900;
	}
</style>
