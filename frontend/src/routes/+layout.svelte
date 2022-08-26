<script>
	import '../app.css';
	import SideBar from '$lib/SideBar.svelte';

	export let data;
</script>

<div>
	<SideBar packages={data.packages} />

	<div class="pl-64 flex flex-col flex-1">
		<main class="flex-1">
			<div class="py-6">
				<slot />
			</div>
		</main>
	</div>
</div>
