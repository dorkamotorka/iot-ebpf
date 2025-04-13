import matplotlib.pyplot as plt

def create_throughput_graph(base_throughput, ebpf_min, ebpf_max):
    """
    Creates a bar graph comparing base throughput and eBPF throughput range.

    Args:
        base_throughput: Base throughput in Mbits/sec (float).
        ebpf_min: Minimum eBPF throughput in Mbits/sec (float).
        ebpf_max: Maximum eBPF throughput in Mbits/sec (float).
    """

    categories = ['Base Throughput', 'Throughput with eBPF (flat)']
    values = [base_throughput, (ebpf_min + ebpf_max) / 2]  # use the average for the bar, show range in error bars
    error = [(0, (ebpf_max - ebpf_min) / 2)]  # error bar range

    plt.figure(figsize=(8, 6))
    plt.bar(categories, values, yerr=error, capsize=5)  # add error bars

    plt.ylabel('Throughput (Mbits/sec)')
    plt.title('Base vs. Throughput with eBPF (flat)')
    plt.ylim(0, max(ebpf_max, base_throughput) * 1.05)  # Start y-axis at 0
    plt.grid(True, which='both', linestyle='--', linewidth=0.5) #add grid
    plt.tight_layout()  # avoid labels being cut off

    plt.show()

base_throughput = 931
ebpf_min = 890
ebpf_max = 920

create_throughput_graph(base_throughput, ebpf_min, ebpf_max)
