<script>
	import '../app.css';
	import SideBar from '$lib/SideBar.svelte';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	export let data;
	onMount(() => {
		goto(`/package/${data?.packages[0]}`);
	});
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
